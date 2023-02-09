"""
# dizi = [22,27,16,2,18,6] -> Insertion Sort türüne göre aşamaları
1- İlk önce ilk iki elemana bakarız. 22, 27'den küçük olduğu için yerinde kalır. Bu aşama sonundaki dizinin hali [22,27,16,2,18,6].

2- İkinci aşamada 27 ile 16'ya bakarız. 27 16'dan büyük olduğu için 16, 1.inci indekse geçer. Daha sonra 16 ile 22'e bakarız. 16, 22'den küçük olduğu için
16 elemanı ilk sırayı alır. Bu aşama sonundaki dizinin hali [16,22,27,2,18,6].

3- Üçüncü aşamada 27 ile 2'ye bakarız. 27, 2'den büyük olduğu için 2, 2.ci indekse geçer. Daha sonra 2 ile 22ye bakarız. 22, 2'den büyük olduğu için 2, 1.ci indekse
geçer. En sonunda 2 ile 16'ya bakarız. 16, 2 den büyük olduğu için 2, 0.cı indekse geçer. Bu aşama sonundaki dizinin hali [2,16,22,27,18,6].

4- Dördüncü aşamada 27 ile 18'e bakarız. 27, 18'den büyük olduğu için 18, 3.cü indekse geçer. Daha sonra 22 ile 18'e bakarız. 22, 18'den büyük olduğu için 18, 2.ci
indekse geçer. Daha sonra 18 ile 16'ya bakarız. 18, 16'dan büyük olduğu için 18 yerinde kalır. Bu aşama sonundaki dizinin hali [2,16,18,22,27,6].

5- Beşinci aşamada 27 ile 6'ya bakarız. 27, 6'dan büyük olduğu için 6, 4.cü indekse geçer. Daha sonra 6 ile 22'e bakarız. 22, 6'dan büyük olduğu için 6, 3.cü indekse geçer. Böyle
karşılaştıra karşılaştıra 6 0.cı indekse geçer. Bu aşama sonundaki dizinin hali [2,6,16,18,22,27] olur.


Bu sıralamanın big-o notasyonu ise best-case için "O(n)", worst-case için ise "O(n^^2)'dir."

18 sayısı sıralanmış dizinin ortasında olduğu için average-case kapsamına girer.



#[7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.

1- İlk eleman baz alınır ve dizinin her elemanı baştan sona taranır. Tüm tarama sonucunda en küçük eleman 2 olduğundan 2, en başa atanır. [2,3,5,8,7,9,4,15,6]
2- "3" elemanı baz alınır ve dizinin her elemanı baştan sona taranır. Tüm tarama sonucunda kendisinden daha küçük eleman olmadığından olduğu yerde kalır. [2,3,5,8,7,9,4,15,6]
3- "5" elemanı baz alınır ve dizinin her elemanı baştan sona taranır. Tüm tarama sonucunda kendisinden daha küçük olan "4" elemanı kendisinin yerine geçer. [2,3,4,8,7,9,5,15,6]
4- "8" elemanı baz alınır ve dizinin her elemanı baştan sona taranır. Tüm tarama sonucunda kendisinden daha küçük olan "5" elemanı kendisinin yerine geçer. [2,3,4,5,7,9,8,15,6]

"""
