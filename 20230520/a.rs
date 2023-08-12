use proconio::input;

fn main() {
    input! {
        hp: i64,
        pw: i64,
    }

    let mut divided = hp / pw;
    let rest = hp % pw;

    if rest != 0 {
        divided = divided + 1;
    }

    println!("{}", divided)
}
