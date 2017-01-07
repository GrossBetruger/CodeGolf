package com.company;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

/**
 * Created by oren on 07/01/17.
 */
public class PrimeCalc {

    public static boolean isPrimeRange(int n, Integer[] range){
        int start = range[0];
        int end = range[range.length-1];
        return IntStream.rangeClosed(start, end).allMatch(i -> n % i != 0);
    }

    public static List<ArrayList<Integer>> sliceRange(List <Integer> range, int sliceSize){
        ArrayList<ArrayList<Integer>> slices = new ArrayList<>();
        while (range.size() - sliceSize > 0) {
            slices.add(new ArrayList<>(range.subList(0, sliceSize)));
            range = new ArrayList<>(range.subList(sliceSize, range.size()));
        }
        slices.add(new ArrayList<>(range.subList(0, range.size())));
        return slices;
    }

//    public static int [] toIntArray (List intList){
//        List<Integer> integerList =  new ArrayList<>(intList);
//        Integer[] integerArray = integerList.toArray(new Integer[0]);
//    }

}
