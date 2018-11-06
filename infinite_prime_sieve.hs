--ghc 7.10

prime :: Integer -> Bool 
prime x = not (elem 0 (map (x `mod`) [2..x-1])) 
 
main = print $ take 100 (filter prime [1..])

