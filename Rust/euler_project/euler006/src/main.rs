fn main() {
    let difference : u64 = (1..101).sum::<u64>().pow(2) - (1..101).map(|x : u64| {x.pow(2)}).sum::<u64>();
    println!("{:?}", difference);
}
