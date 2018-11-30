

naturals = [1..100]

layer xs
  | length xs < 2 = []
  | otherwise = [head xs + (head . tail) xs] ++ layer(drop 1 xs)

grid xs = [(head . layer) xs] ++ grid (layer xs)

main = print (take 10 (grid naturals))