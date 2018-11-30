

naturals = [1..10]

layer :: [Int] -> [Int]
layer xs
  | length xs < 2 = []
  | otherwise = [head xs + (head . tail) xs] ++ layer(drop 1 xs)


main = print $ layer $ layer $ layer $ layer naturals