fn main() {
    let mut sieve : Vec<bool> = vec![true; 1_000_000];
    sieve[0] = false;
    sieve[1] = false;
    println!("finished vector creation, beginning prime search...");
    let mut num : usize = 0;
    while num < sieve.len() - 1 {
        num += 1;
        if !sieve[num] {
            continue;
        }
        let mut c = 2;
        while num * c < sieve.len() - 1 {
            sieve[(num * c)] = false;
            c += 1;
        }
    }
    println!("primes found, creating vector of primes...");
    let mut primes: Vec<usize> = vec!();
    for (num, prime) in sieve.iter().enumerate() {
        if *prime {
            primes.push(num);
        }
    }
    //println!("{:?}",primes);
    println!("found {} primes",primes.len());
    if primes.len() > 10_000 {
        println!("10_001st prime number is {}",primes[10_000]);
    }
}
