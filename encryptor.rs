
fn xor(x: i32, y: i32) -> i32 {
    x ^ y
}

fn charxor(x: char, y: char) -> char {
    return (x as u8 ^ y as u8) as char
}


fn xor_u8(x: u8, y: u8) -> u8 {
    x ^ y
} 

fn xor_u8_vec(secret: Vec<u8>, passwd: Vec<u8>) ->  String {
        
    let mut result = Vec::new(); 
    for (i, c) in secret.iter().enumerate(){
        let pass_idx = i % passwd.len();
        result.push(secret[i] ^ passwd[pass_idx]);
    }
    return String::from_utf8(result).unwrap();
}


fn main() {
    let x = 1;
    let y = 2;
    let input = "secret";
    let inpt_chars:Vec<char> = input.chars().collect();
    let inpt_ords:Vec<u8> = inpt_chars.into_iter().map(|x| x as u8).collect();

    let password = "pass";
    let passwd_chars:Vec<char> = password.chars().collect();
    let passwd_ords:Vec<u8> = passwd_chars.into_iter().map(|x| x as u8).collect();

    println!("xor {} {} = {}", x, y, xor(x, y));
    

    println!("cryptext: {}", xor_u8_vec(inpt_ords, passwd_ords));
}

