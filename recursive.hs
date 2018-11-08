maxi :: (Ord n) => [n] -> n; maxi [n] = n; maxi (x:xs) = max x (maxi xs)

main = print $ "maximum [7, 23, 3, 18]: " ++ show (maxi [7, 23, 3, 18])
