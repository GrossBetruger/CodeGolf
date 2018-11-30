

{-

imagine a grid that starts with a diagonal of the naturals 1..
and then all other spaces in the grid are filled by summing the
numbers directly up and to the right of that space

like that:

1

|
v

3 <---  2

|       |
v       v

8 <---  5  <--- 3

|       |       |
v       v       v

20 <--- 12 <--- 7 <--- 4

|       |       |      |
V       v       v      v

48 <--- 28 <--- 16 <--- 9 <--- 5

the following code would output the leftmost column of this grid:
1,3,8,20,48,112,256,576,...

-}

naturals = [1..102]

layer xs
  | length xs < 2 = []
  | otherwise = [head xs + (head . tail) xs] ++ layer(drop 1 xs)

firstColumn xs = [head xs] ++ firstColumn (layer xs)

main = print (take 10 (firstColumn naturals))