use std::io::BufRead;
use std::io::{self, Error};
fn main() {
    println!("Hello, world!");
    let F: String = String::from("AAAAA");
    println!("{}", F);
    let ary: [i64; 4] = [7, 7, 7, 7];
    for i in 0..4 {
        let x = ary[i] as u16;
        println!("{}", x);
    }

    let mut calories: Vec<i64> = vec![];
    let stdin = io::stdin();
    let mut calorie_count = 0;
    let mut count = 0;
    for mut line in stdin.lock().lines() {
        if !(line.as_mut().unwrap() == "\r"
            || line.as_mut().unwrap() == "\n"
            || line.as_mut().unwrap() == "")
        {
            println!("{}", line.as_mut().unwrap());
            calorie_count += line.unwrap().parse::<i64>().unwrap();
        } else {
            calories.insert(calories.len(), calorie_count);
            calorie_count = 0;
        }
        count += 1;
    }

    let mut max = <i64>::from(calories[0]);
    println!("{}", max);

    let mut maxtwo = calories[0];
    let mut maxthree = calories[0];

    for line in calories {
        if line > max {
            maxthree = maxtwo;
            maxtwo = max;
            max = line;
        } else if line > maxtwo {
            maxthree = maxtwo;
            maxtwo = line;
        } else if line > maxthree {
            maxthree = line;
        }
    }

    // println!("{}",(max + maxtwo + maxthree)/ 3);
    println!("{}", max);
    println!("{}", maxtwo);
    println!("{}", maxthree);
}
