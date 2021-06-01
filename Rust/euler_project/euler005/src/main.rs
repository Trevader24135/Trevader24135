fn main() {
    let mut num: u64 = 0;
    
    'num_loop: loop {
        num += 20;
        for i in (3..20).rev() {
            if num % i != 0 {
                continue 'num_loop;
            }
        }
        break;
    }
    println!("{}",num);
}
