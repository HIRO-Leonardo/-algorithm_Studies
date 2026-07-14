package org.example;

import java.util.ArrayList;
import java.util.List;

public class BinarySearch {
    public static Integer buscaBinaria(ArrayList<Integer> lista, Integer valor){

        Integer inicio = 0;
        Integer fim = lista.size() - 1;

        while (inicio <= fim){
            Integer m = (inicio + fim) / 2;
            System.out.println("Resultado de M: " + m);
            if (lista.get(m) > valor){
                fim = m - 1;
            } else if (lista.get(m) < valor) {
                inicio = m + 1;
            }else {
                return m;
            }

        }
        return -1;
    }

    public static void main(String[] args) {
        ArrayList<Integer> nums = new ArrayList<>(List.of(1,2,3,4,5,6,7,8,9,10,11,12,13));
        Integer resultado = buscaBinaria(nums,8);
        System.out.println(resultado);
    }

}
