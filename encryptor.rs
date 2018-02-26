use std::io::{self, BufRead};
use std::env;


fn xor(x: i32, y: i32) -> i32 {
    x ^ y
}

fn charxor(x: char, y: char) -> char {
    return (x as u8 ^ y as u8) as char
}


fn xor_u8(x: u8, y: u8) -> u8 {
    x ^ y
} 

fn xor_u8_vec(secret: Vec<u8>, passwd: Vec<u8>) ->  Vec<u8> {
        
    let mut result = Vec::new(); 
    for (i, c) in secret.iter().enumerate(){
        let pass_idx = i % passwd.len();
        result.push(secret[i] ^ passwd[pass_idx]);

    }
    return result;
}

fn readUserInpt() -> String{

    let mut line = String::new();
    let stdin = io::stdin();
    println!("pls enter password...");
    stdin.lock().read_line(&mut line).expect("Could not read line");
    line.pop();
    return line;
}


fn main() {

    let args: Vec<String> = env::args().collect();

    //let mut line = readUserInpt();
    let secret = vec![3,4,16,1,21,21];

    let mut line = &args[1];

    println!("length {}", line.len());

    //let secret_chars:Vec<char> = secret.chars().collect();
    //let secret_ords:Vec<u8> = secret_chars.into_iter().map(|x| x as u8).collect();

    //let password = "pass";
    let line_chars:Vec<char> = line.chars().collect();
    let line_ords:Vec<u8> = line_chars.into_iter().map(|x| x as u8).collect();


    let res:Vec<u8> = xor_u8_vec(secret, line_ords);

    for x in &res {
        print!("{},", x);
    }

    println!("\n{}", String::from_utf8(res).unwrap());

}

