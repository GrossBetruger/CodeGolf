package com.company;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ForkJoinPool;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import static com.company.PrimeCalc.isPrimeRange;
import static com.company.PrimeCalc.sliceRange;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Runtime runtime = Runtime.getRuntime();
        int numberOfProcessors = runtime.availableProcessors();
        System.out.println("number of cores: " + numberOfProcessors);


        int primeSuspect = 15486883;
        Double squareRoot = (Math.ceil(Math.sqrt(primeSuspect)));
        int optimizedMax = squareRoot.intValue();

        List<Integer> suspRange = IntStream.range(2, primeSuspect).boxed().collect(Collectors.toList());
        int sliceSize = primeSuspect/400;
        System.out.println("slice size: " + sliceSize);
        List<ArrayList<Integer>> slices = sliceRange(suspRange, sliceSize);
        System.out.println("number of jobs: " + slices.size());


        ForkJoinPool forkJoinPool = new ForkJoinPool(numberOfProcessors);
        try {
            long startTime = System.currentTimeMillis();

            System.out.println(
            forkJoinPool.submit(() ->
                    slices.stream().parallel().allMatch(subRange -> isPrimeRange(primeSuspect, subRange.toArray(new Integer[0])))
            ).get());
            long stopTime = System.currentTimeMillis();
            long elapsedTime = stopTime - startTime;
            System.out.println("took me: " + elapsedTime/1000.);

        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }

    }
}
