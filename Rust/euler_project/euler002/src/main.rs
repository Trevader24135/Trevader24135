fn main() {
    let mut fibnum = [1,2];
    let mut even_sum = 2;

    while fibnum[1] < 4_000_000 {
        let resultant = fibnum[0] + fibnum[1];
        fibnum[0] = fibnum[1];
        fibnum[1] = resultant;
        if resultant % 2 == 0 {
            even_sum += resultant;
        }
    }
    println!("{}",even_sum);
}
