""" [16,21,11,8,12,22] -> Merge Sort

#Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.

1. Öncelikle dizi ikiye ayrılır. [16,21,11] / [8,12,22]
2. Sonrasında bu iki dizi de kendi içlerinde ikiye ayrılır. [16,21] - [11] / [8,12] - [22]
3. Diziler iki elemanlı olduğu için daha fazla bölünmez. Bu parçalar sıraya bağlı olarak birleşmeye başlar. [11,16,21] / [8,12,22]
4. Bu iki dizi de yine sıralamaya bağlı olarak birleşir. [8,11,12,16,21,22]

#Big-O gösterimini yazınız.

Tüm caseler için(best-case, average-case, worst-case) O(nlogn)'dir.


"""