/*
 *  Copyright 2023 The original authors
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */
package dev.morling.onebrc;

public class RoundFloats {
    public static void main(String[] args) {
        double[] floats = {
                1.5,
                -1.5,
                2.5,
                -2.5,
                75.312,
                -12.097,
                54.893,
                -82.645,
                39.781,
                -66.227,
                88.506,
                20.399,
                15.127,
                -45.884,
                92.750,
                -31.419,
                63.268,
                -96.922,
                -8.556,
                5.795,
                69.332,
                -53.460,
                -71.139,
                82.168,
        };

        System.out.println("Original Floats:");
        for (double f : floats) {
            System.out.println(f);
        }

        System.out.println("\nRounded Floats:");
        for (double f : floats) {
            double roundedValue = Math.round(f);
            System.out.println(roundedValue);
        }
    }
}
