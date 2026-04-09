package com.app;

public class App {
    public static void main(String[] args) {
        System.out.println("Baseline CI/CD App Running!");
    }
    // AND: Returns true if both conditions are met
    public boolean evaluateAND(boolean a, boolean b) { return a && b; }
    // OR: Returns true if at least one condition is met
    public boolean evaluateOR(boolean a, boolean b) { return a || b; }
    // NOT: Reverses the input
    public boolean evaluateNOT(boolean a) { return !a; }
}
