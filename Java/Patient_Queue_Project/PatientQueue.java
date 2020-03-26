/*
 *  
 *AUTHOR: Caroline McCormick
 *FILE: PatientQueue.java 
 *ASSIGNMENT: Programming Assignment 9 - PatientQueue  
 *COURSE: CSC 210; Fall 2019 
 *PURPOSE: This class implements a priority queue of Patient objects using a binary
 *minimum heap. A priority queue is a queue that is ordered by the priority assigned
 *to each Patient. The lowest number (highest priority) is at the front of the
 *queue.
 * 
 */

public class PatientQueue {

    private static final int DEFAULT_CAPACITY = 11;
    private Patient[] array;
    private int size;
    private int capacity;

    /*
     * Purpose: This method constructs a new instance of PatientQueue by
     * creating a priority queue with an initial capacity that is the 
     * default capacity.
     * 
     * @param None
     * 
     * @return None
     */
    public PatientQueue() {
        array = new Patient[DEFAULT_CAPACITY];
        size = 0;
        capacity = DEFAULT_CAPACITY;
    }

    /*
     * Purpose: This method doubles the size of the underlying array and the
     * capacity of the priority queue.
     * 
     * @param None
     * 
     * @return None
     */
    private void doubleArray() {
        Patient[] newArray = new Patient[capacity * 2];
        for (int i = 0; i <= size; i++) {
            newArray[i] = array[i];
        }
        array = newArray;
        capacity *= 2;
    }

    /*
     * Purpose: This method bubbles a Patient up (i.e. moves the Patient) to the
     * front of the priority queue until their priority is no longer more urgent
     * than their parent's (the parent of a Patient is the Patient at position i/2
     * in the underlying array where i is the index of the Patient being moved).
     * 
     * @param index, the index in the underlying array that the Patient to be
     * bubbled up is at.
     * 
     * @return None
     */
    private void bubbleUp(int index) {
        while (index < size + 1 && index > 1) {
            Patient parent = array[index / 2];
            Patient child = array[index];
            if (comparePatients(parent, child) > 0) {
                array[index / 2] = child;
                array[index] = parent;
                index = index / 2;
            } else {
                return;
            }
        }
    }

    /*
     * Purpose: This method bubbles a Patient down (i.e. moves the Patient) to 
     * the back of the priority queue until their priority is no longer less 
     * urgent than their child's (a Patient has two children, one at i*2 and 
     * one at i*2 + 1 where i is the index in the underlying array of the Patient
     * being moved).
     * 
     * @param index, the index in the underlying array that the Patient to be
     * bubbled down is at.
     * 
     * @return None
     */
    private void bubbleDown(int index) {
        while (index * 2 <= size) {
            Patient parent = array[index];
            Patient child1 = array[index * 2];
            Patient child2 = null;
            if ((index * 2 + 1) <= size) {
                child2 = array[index * 2 + 1];
            }
            if (child2 == null) {
                if (comparePatients(parent, child1) > 0) {
                    array[index * 2] = parent;
                    array[index] = child1;
                }
                index *= 2;
            } else {
                int diff = comparePatients(child1, child2);
                if (diff < 0) {
                    if (comparePatients(parent, child1) > 0) {
                        array[index * 2] = parent;
                        array[index] = child1;
                        index *= 2;
                    } else {
                        return;
                    }
                } else if (diff > 0) {
                    if (comparePatients(parent, child2) > 0) {
                        array[index * 2 + 1] = parent;
                        array[index] = child2;
                        index *= 2 + 1;
                    } else {
                        return;
                    }
                }
            }
        }
    }

    /*
     * Purpose: This method indicates the priority order of two patients, i.e.
     * if one Patient's priority is more urgent than the other, or if they have
     * the same priority, which name should go first.
     * 
     * @param patient1, the first Patient to compare.
     * 
     * @param patient2, the second Patient to compare.
     * 
     * @return -1, if patient1 is more urgent than patient2.
     * 
     * @return 1, if patient2 is more urgent than patient1.
     */
    private int comparePatients(Patient patient1, Patient patient2) {
        if (patient1.priority < patient2.priority) {
            return -1;
        } else if (patient2.priority < patient1.priority) {
            return 1;
        } else {
            if (patient1.name.compareTo(patient2.name) < 0) {
                return -1;
            } else {
                return 1;
            }
        }
    }

    /*
     * Purpose: Given a name and a priority, this method adds a Patient to the
     * priority queue while maintaining the correct priority order.
     * 
     * @param name, the name of the Patient.
     * 
     * @param priority, the priority of the Patient.
     * 
     * @return None
     */
    public void enqueue(String name, int priority) {
        if (size + 1 >= capacity) {
            doubleArray();
        }
        Patient patient = new Patient(name, priority);
        array[size + 1] = patient;
        size += 1;
        bubbleUp(size);
    }

    /*
     * Purpose: Given a Patient object, this method adds a Patient to the
     * priority queue while maintaining the correct priority order.
     * 
     * @param patient, the patient to be added.
     * 
     * @return None
     */
    public void enqueue(Patient patient) {
        if (size + 1 >= capacity) {
            doubleArray();
        }
        array[size + 1] = patient;
        size += 1;
        bubbleUp(size);
    }

    /*
     * Purpose: This method removes the most urgent Patient from the priority
     * queue, throwing an exception if the queue is empty.
     * 
     * @param None
     * 
     * @return frontPatient, the name of the Patient as a string.
     */
    public String dequeue() throws Exception {
        if (isEmpty()) {
            throw new Exception("Empty queue.");
        }
        String frontPatient = array[1].name;
        array[1] = array[size];
        array[size] = null;
        size -= 1;
        bubbleDown(1);
        return frontPatient;
    }

    /*
     * Purpose: This method returns the most urgent Patient's name without
     * removing them from the queue. It throws an exception if the queue is
     * empty.
     * 
     * @param None
     * 
     * @return array[1].name, the name of the patient as a string.
     */
    public String peek() throws Exception {
        if (isEmpty()) {
            throw new Exception("Empty queue.");
        }
        return array[1].name;
    }

    /*
     * Purpose: This method returns the most urgent Patient's priority without
     * removing them from the queue. It throws an exception if the queue is
     * empty.
     * 
     * @param None
     * 
     * @return array[1].priority, the priority of the Patient.
     */
    public int peekPriority() throws Exception {
        if (isEmpty()) {
            throw new Exception("Empty queue.");
        }
        return array[1].priority;
    }

    /*
     * Purpose: Given a Patient name and new priority, this method finds the
     * Patient in the queue, if they're in it, and changes their priority while
     * maintaining the priority queue order.
     * 
     * @param name, the name of the Patient to have their priority changed.
     * 
     * @param newPriority, the new priority that the Patient will now have.
     * 
     * @return None
     */
    public void changePriority(String name, int newPriority) {
        Patient patient = new Patient(name, newPriority);
        int index = 0;
        int oldPriority = 0;
        for (int i = 1; i <= size; i++) {
            if (array[i].name.equals(name)) {
                index = i;
                oldPriority = array[i].priority;
            }
        }
        if (index > 0) {
            array[index] = patient;
            if (newPriority < oldPriority) {
                bubbleUp(index);
            } else if (newPriority > oldPriority) {
                bubbleDown(index);
            }
        }
    }

    /*
     * Purpose: This method checks if the priority queue is empty or not.
     * 
     * @param None
     * 
     * @return true, if the queue is empty.
     * 
     * @return false, if the queue is not empty.
     */
    public boolean isEmpty() {
        if (size > 0) {
            return false;
        }
        return true;
    }

    /*
     * Purpose: This method returns the number of Patients in the priority
     * queue.
     * 
     * @param None
     * 
     * @return size, the number of Patients in the priority queue.
     */
    public int size() {
        return size;
    }

    /*
     * Purpose: This method clears the priority queue of all Patients.
     * 
     * @param None
     * 
     * @return None
     */
    public void clear() {
        size = 0;
    }

    /*
     * Purpose: This method returns a string representation of the priority
     * queue with a comma separated list of each Patient represented as their
     * name and their priority.
     * 
     * @param None
     * 
     * @return patientString, the string representation of the priority queue.
     */
    @Override
    public String toString() {
        String patientString = "{";
        if (size > 0) {
            for (int i = 1; i < size; i++) {
                patientString += array[i].name + " (" + array[i].priority
                        + "), ";
            }
            patientString += array[size].name + " (" + array[size].priority
                    + ")";
        }
        return patientString + "}";
    }

}
