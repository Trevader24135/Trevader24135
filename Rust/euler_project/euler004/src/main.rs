fn main() {
    let mut largest = 0;
    
    for i in 100..999 {
        for n in 100..999 {
            let product = i * n;
            if is_palindromic(&(product).to_string()) && product > largest {
                largest = product;
            }
        }
    }
    println!("{}",largest);
}

fn is_palindromic(string : &str) -> bool {
    let character = string.chars();
    let character_reversed = string.chars().rev();

    for (forward, reverse) in character.zip(character_reversed) {
        if forward != reverse {
            return false;
        }
    }
    true
}
