"""
#[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.

1- 7 elemanını root olarak seçeriz. 5 elemanı 7'den küçük olduğu için 7'in sol altına yazılır.

                                                    7
                                                5

2- 1 elemanı root'tan küçük olduğu için sol alta, 5'ten de küçük olduğu için 5'in sol altına yazılır.

                                                    7
                                                5
                                            1

3- 8 elemanı root'tan büyük olduğu için sağ alta yazılır.

                                                    7
                                                5       8
                                            1

4- 3 elemanı root'tan küçük olduğu için sol alta, 5'den de küçük olduğu için sol alta, 1'den büyük olduğu için 1'in sağ altına yazılır.

                                                    7
                                                5       8
                                             1
                                                3

5- 6 elemanı root'tan küçük olduğu için sol alta, 5'den büyük olduğu için 5'in sağ altına yazılır.

                                                    7
                                                5       8
                                             1    6
                                              3

6- 0 elemanı root'tan küçük olduğu için sol alta, 5'den de küçük olduğu için sol alta, 1'den küçük olduğu için 1'in sol altına yazılır.

                                                    7
                                                5       8
                                             1    6
                                           0  3

7- 9 elemanı root'tan büyük olduğu için sağ alta, 8'den büyük olduğu için 8'in sağ altına yazılır.

                                                    7
                                                5       8
                                             1    6        9
                                           0  3

8- 4 elemanı root'tan küçük olduğu için sol alta, 5'den de küçük olduğu için sol alta, 1'den büyük olduğu için sağ alta, 3'den büyük olduğu için 3'ün sağ altına yazılır.

                                                    7
                                                5       8
                                             1    6        9
                                           0  3
                                                4

9- 2 elemanı root'tan küçük olduğu için sol alta, 5'den de küçük olduğu için sol alta, 1'den büyük olduğu için sağ alta, 3'den küçük olduğu için 3'ün sol altına yazılır.

                                                    7
                                                5       8
                                             1    6        9
                                           0  3
                                             2  4
"""