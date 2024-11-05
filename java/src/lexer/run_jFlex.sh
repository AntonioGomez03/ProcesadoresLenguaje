#!/bin/sh

jflex LenguajeGec.fle

javac analisisLexico.java

java analisisLexico ejemplo.gec
