
/*
 *  
 *AUTHOR: Caroline McCormick
 *FILE: PA2Main.java 
 *ASSIGNMENT: Programming Assignment 2 - Job Skills  
 *COURSE: CSC 210; Fall 2019 
 *PURPOSE: This program reads in a file containing information about various jobs, and it takes
 *a command (CATCOUNTS or LOCATIONS) to determine different outputs. If the command CATCOUNTS is
 *given, the program will print out all the categories of jobs that are in the given file as well
 *as the number of jobs in each category. If the command LOCATIONS is given, the user must also 
 *provide a specific category, and the program will print out all the locations in that specific
 *category that have job openings as well as the number of openings at each location. All printed
 *out data is in alphabetical order.
 *
 *Usage:
 *$ java PA2Main infileName COMMAND optional
 *
 *infileName is the name of the job input file with the following format
 *-------- EXAMPLE INPUT ----------------
 * Company,Title,Category,Location,Responsibilities,Minimum Qualifications,Preferred Qualifications
 * Google,TitleA,CategoryX,Tel Aviv,Everything and the rest,BS,MS
 * Google,TitleB,CategoryY,Houston,Everything and the rest,BS,MS
 * Google,TitleC,CategoryX,Jonesboro,Everything and the rest,BS,MS
 * 
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class PA2Main {

    public static void main(String[] args) {
        Map<String, Map<String, Integer>> jobDataMap = createJobMap(args[0]);

        if (args[1].toUpperCase().equals("LOCATIONS")) {
            executeLocations(jobDataMap, args[2]);
        } else if (args[1].toUpperCase().equals("CATCOUNT")) {
            executeCatcount(jobDataMap);
        } else {
            System.out.println("Invalid Command");
        }
    }

    /*
     * Purpose: This method reads the input job file and creates a map of job
     * categories (strings)
     * mapped to a map of locations (strings) mapped to the number of open
     * positions at a location
     * (integers).
     * 
     * @param jobFileName, is the file name that contains all of the job data.
     * 
     * @return jobDataMap, is a map of categories to a map of locations to the
     * number of open positions at each location.
     */
    public static Map<String, Map<String, Integer>> createJobMap(
            String jobFileName) {
        Scanner jobFile = null;

        // make sure file exists
        try {
            jobFile = new Scanner(new File(jobFileName));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        Map<String, Map<String, Integer>> jobDataMap = new HashMap<String, Map<String, Integer>>();
        
        // create jobDataMap by going through each line of the file
        while (jobFile.hasNext()) {
            String currentLine = jobFile.nextLine();
            String[] splitLine = currentLine.split(",");

            // making sure to exclude the header in the file
            if (splitLine[0].toUpperCase().equals("COMPANY")) {
                currentLine = jobFile.nextLine();
                splitLine = currentLine.split(",");
            }
            String category = splitLine[2];
            String location = splitLine[3];

            if (!jobDataMap.containsKey(category)) {
                Map<String, Integer> innerMap = new HashMap<String, Integer>();
                innerMap.put(location, 1);
                jobDataMap.put(category, innerMap);
            } else {
                if (!jobDataMap.get(category).containsKey(location)) {
                    jobDataMap.get(category).put(location, 1);
                } else {
                    int currentCount = jobDataMap.get(category).get(location);
                    jobDataMap.get(category).put(location, currentCount + 1);
                }
            }
        }
        return jobDataMap;
    }

    /*
     * Purpose: This method handles the case in which the command CATCOUNT is
     * given. It prints
     * out all the categories in alphabetical order along with the number of
     * jobs in each category.
     * 
     * @param jobDataMap, is a map of categories to a map of locations to the
     * number of open positions at each location.
     * 
     * @return nothing; Prints out categories and number of jobs in each
     * category.
     */
    public static void executeCatcount(
            Map<String, Map<String, Integer>> jobDataMap) {
        System.out.println("Number of positions for each category");
        System.out.println("-------------------------------------");

        // sort categories alphabetically
        List<String> sortedCategories = new ArrayList<String>(
                jobDataMap.keySet());
        Collections.sort(sortedCategories);

        // sorts numbers of jobs according to sorted categories
        for (String category : sortedCategories) {
            Integer numJobs = 0;
            for (Integer count : jobDataMap.get(category).values()) {
                numJobs += count;
            }
            System.out.println(category + ", " + numJobs);
        }
    }

    /*
     * Purpose: This method handles the case in which the command LOCATIONS is
     * given. For a given
     * category, it prints out all the locations in alphabetical order along
     * with the number of
     * positions open in each category.
     * 
     * @param jobDataMap, is a map of categories to a map of locations to the
     * number of open positions at each location.
     * 
     * @param category, is the category which the user wants all the location
     * data.
     * 
     * @return nothing; Prints out locations and number of positions at each
     * location.
     */
    public static void executeLocations(
            Map<String, Map<String, Integer>> jobDataMap, String category) {
        System.out.println("LOCATIONS for category: " + category);
        System.out.println("-------------------------------------");

        // sort locations alphabetically
        if (jobDataMap.containsKey(category)) {
            List<String> sortedLocations = new ArrayList<String>(
                    jobDataMap.get(category).keySet());
            Collections.sort(sortedLocations);

            for (String loc : sortedLocations) {
                int numPositions = jobDataMap.get(category).get(loc);
                System.out.println(loc + ", " + numPositions);
            }
        }

    }
}


