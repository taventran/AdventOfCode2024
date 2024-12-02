use std::fs::File;
use std::io::{self, BufRead};

//fn bubble_sort(Vec<i32> list1, Vec<i32> list2) -> Vec<i32> {
//
//}

fn main() {
    let file = File::open("input.txt").expect("Could not read file");
    let reader = io::BufReader::new(file);
    let mut list1: Vec<i32>;
    let mut list2: Vec<i32>;
    for line in reader.lines() {
        let temp = line.expect("fail clone").clone().split(' ');
        for num in temp {
            println!("{}", num)
        }
    }
}
