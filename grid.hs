

naturals = [1..102]

layer xs
  | length xs < 2 = []
  | otherwise = [head xs + (head . tail) xs] ++ layer(drop 1 xs)

firstColumn xs = [(head . layer) xs] ++ firstColumn (layer xs)

main = print (take 10 (firstColumn naturals))