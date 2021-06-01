fn main() { 
    const NUMBER: u64 = 600851475143; // 600851475143

    let mut primes: Vec<u64> = Vec::new(); // turns out that I want to use vectors for primes, not arrays. vectors are stored on the heap, arrays stored on the stack

    for i in 2..((NUMBER as f64).sqrt() as u64) {
        if NUMBER % i != 0 {
            continue;
        }
        let mut prime = true;
        for n in primes.iter() {
            if i % n == 0 {
                prime = false;
                break;
            }
        }
        if prime {
            primes.push(i);
        }
    }

    println!("{:?}",primes);
}
