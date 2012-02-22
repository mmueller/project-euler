(def names (vec (sort (load-file "inputs/p22.txt"))))

(def score {
    \A 1 \B 2 \C 3 \D 4 \E 5 \F 6 \G 7 \H 8 \I 9 
    \J 10 \K 11 \L 12 \M 13 \N 14 \O 15 \P 16 \Q 17 \R 18
    \S 19 \T 20 \U 21 \V 22 \W 23 \X 24 \Y 25 \Z 26 } )

(def scoreWord (fn [word] (reduce + (map score word))))

(print (reduce +
    (for [index (range (count names))]
        (* (scoreWord (get names index)) (+ index 1)))) "\n")

(def recursiveSolution (fn [names index]
    (if names (+ (* (scoreWord (first names)) index)
        (recursiveSolution (rest names) (+ index 1))) 0)))
(print (recursiveSolution names 1) "\n")
