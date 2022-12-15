import 'dart:io';
import 'dart:core';
bool touching(List<int> head_position,List<int> tail_position) {
	if ( head_position[0] - tail_position[0] <=1 
			&& head_position[0]-tail_position[0]>=-1){
		if ( head_position[1] - tail_position[1] <=1 
				&& head_position[1]-tail_position[1]>=-1){
			return true;

		}
	}
	return false;
}

List<int> step(String s, List<int> position) {
	if (s=='U') {
		position[0]+=1;
	}
	if (s=='D') {
		position[0]-=1;
	}
	if (s=='R') {
		position[1]+=1;
	}
	if (s=='L') {
		position[1]-=1;
	}
	return position;
}

List<int> step_tail( List<int> head_position , List<int> tail_position ) {
	int head_row = head_position[0];
	int  head_column = head_position[1];
	int tail_row = tail_position[0];
	int tail_column = tail_position[1];
	bool same_row = (head_row==tail_row);
	bool same_column = (head_column==tail_column);

	if (same_row && ! same_column){
		if (head_column>tail_column){
			tail_position[1]++;
		}
		else{
			tail_position[1]--;
		}
	}
	else if (same_column && ! same_row) {
		if (head_row > tail_row){
			tail_position[0]++;
		}
		else{
			tail_position[0]--;
		}
	}
	else if ( ! same_column && ! same_row ) {
		if (head_column>tail_column && head_row>tail_row){
			tail_position[0]++;
			tail_position[1]++;
		}
		else if (head_column>tail_column && head_row<tail_row){
			tail_position[0]--;
			tail_position[1]++;
		}
		else if (head_column<tail_column && head_row>tail_row){
			tail_position[0]++;
			tail_position[1]--;
		}
		else if (head_column<tail_column && head_row<tail_row){
			tail_position[0]--;
			tail_position[1]--;
		}

	}
	return tail_position;
}


void partone(){
	List<String> places = ['0 0'];
	List<int> head_position=[0,0];
	List<int> tail_position=[0,0];

	for ( var line = stdin.readLineSync();line!=null;line = stdin.readLineSync()){
		int distance = int.parse(line.substring(line.indexOf(' ')+1));
		String direction = line.substring(0,1);

		if ( direction == 'D' ) {
			for ( int i = 0 ; i < distance ; i++ ){
				head_position = step('D',head_position);

				if (! touching ( head_position , tail_position ) ) {
					tail_position = step_tail(head_position,tail_position);
					String place = tail_position[0].toString() + ' ' + tail_position[1].toString();
					var placecheck = places.where((e)=>e==place);
					if (placecheck.length == 0) {
						places.add(place);
					}
				}
			}
		}
		if ( direction == 'U' ) {
			for ( int i = 0 ; i < distance ; i++ ){
				head_position = step('U',head_position);

				if (! touching ( head_position , tail_position ) ) {
					tail_position = step_tail(head_position,tail_position);
					String place = tail_position[0].toString() + ' ' + tail_position[1].toString();
					var placecheck = places.where((e)=>e==place);
					if (placecheck.length == 0) {
						places.add(place);
					}
				}
			}
		}
		if ( direction == 'R' ) {
			for ( int i = 0 ; i < distance ; i++ ){
				head_position = step('R',head_position);

				if (! touching ( head_position , tail_position ) ) {
					tail_position = step_tail(head_position,tail_position);
					String place = tail_position[0].toString() + ' ' + tail_position[1].toString();
					var placecheck = places.where((e)=>e==place);
					if (placecheck.length == 0) {
						places.add(place);
					}
				}
			}
		}
		if ( direction == 'L' ) {
			for ( int i = 0 ; i < distance ; i++ ){
				head_position = step('L',head_position);

				if (! touching ( head_position , tail_position ) ) {
					tail_position = step_tail(head_position,tail_position);
					String place = tail_position[0].toString() + ' ' + tail_position[1].toString();
					var placecheck = places.where((e)=>e==place);
					if (placecheck.length == 0) {
						places.add(place);
					}
				}
			}
		}
	}
	print(places.length);
}

void parttwo(){
	List<int> head_position = [0,0];
		List<int> two = [0,0];
		List<int> three = [0,0];
		List<int> four = [0,0];
		List<int> five = [0,0];
		List<int> six = [0,0];
		List<int> seven = [0,0];
		List<int> eight = [0,0];
		List<int> nine = [0,0];
		List<int> tail_position = [0,0];

		List<List<int>> knots = [head_position,two,three,four,five,six,seven,eight,nine,tail_position];

		List<String> places2 = [];


		for(var line = stdin.readLineSync() ; line != null ; line = stdin.readLineSync()){
			String direction = line.substring(0,line.indexOf(' '));
			int distance = int.parse(line.substring(line.indexOf(' ')+1));
			if ( direction == 'U' ){
				for (int i = 0 ; i < distance ; i++ ) {
				head_position = step('U',head_position);
				for (int j = 0 ; j < 10 ; j++ ) {
					if ( ! touching(knots[i],knots[i+1]) ){
						knots[i+1] = step_tail(knots[i],knots[i+1]);
					}

				}

				
					var check = places2.where((e)=>e==tail_position[0].toString()+' '+tail_position[1].toString());
					if (check.length == 0) {
						places2.add(tail_position[0].toString()+' '+tail_position[1].toString());
				}	}
			}
			if ( direction == 'D' ){
				for (int i = 0 ; i < distance ; i++ ) {
				head_position = step('D',head_position);
				for (int j = 0 ; j < 10 ; j++ ) {
					if ( ! touching(knots[i],knots[i+1]) ){
						knots[i+1] = step_tail(knots[i],knots[i+1]);
					}

				}

				
					var check = places2.where((e)=>e==tail_position[0].toString()+' '+tail_position[1].toString());
					if (check.length == 0) {
						places2.add(tail_position[0].toString()+' '+tail_position[1].toString());
				}	}
			}
			if ( direction == 'R' ){
				for (int i = 0 ; i < distance ; i++ ) {
				head_position = step('R',head_position);
				for (int j = 0 ; j < 10 ; j++ ) {
					if ( ! touching(knots[i],knots[i+1]) ){
						knots[i+1] = step_tail(knots[i],knots[i+1]);
					}

				}

				
					var check = places2.where((e)=>e==tail_position[0].toString()+' '+tail_position[1].toString());
					if (check.length == 0) {
						places2.add(tail_position[0].toString()+' '+tail_position[1].toString());
				}	}
			}
			if ( direction == 'L' ){
				for (int i = 0 ; i < distance ; i++ ) {
				head_position = step('L',head_position);
				for (int j = 0 ; j < 10 ; j++ ) {
					if ( ! touching(knots[i],knots[i+1]) ){
						knots[i+1] = step_tail(knots[i],knots[i+1]);
					}

				}

				
					var check = places2.where((e)=>e==tail_position[0].toString()+' '+tail_position[1].toString());
					if (check.length == 0) {
						places2.add(tail_position[0].toString()+' '+tail_position[1].toString());
				}	}
			}
		}

		print(places2.length);
}

main(){
	partone();
	parttwo();
}
