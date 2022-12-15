import 'dart:io';
bool visible(int x , int y , List<List<int>> trees){
	bool one = true ;
	bool two = true ;
	bool three = true ;
	bool four = true ;
	int value = trees[x][y];
	int check ;
	int i ;
	if ( x == 0 || x == trees.length || y == 0|| y == trees[0].length )return true;
	for ( i = 0 ; i < x ; i++){
		check = trees[i][y];
		if (value <= check ) one = false; 
	}
	if (one) return true;
	for ( i = x+1 ; i < trees.length ; i++){
		check = trees[i][y];
		if (value <= check ) two = false; 
	}
	if (two) return true;
	for ( i = 0 ; i < y ; i++){
		check = trees[x][i];
		if (value <= check) three = false;
	}
	if (three) return true ;
	for ( i = y+1 ; i < trees[0].length ; i++){
		check = trees[x][i];
		if (value <= check) four = false ;
	}

	return four;
}

main(){
	var cur = stdin.readLineSync();
	List<List<int>> trees = [];
	List<int> row = [];
	while(cur!= null ){
		print(cur);
		row = [];
		for ( int i = 0 ; i < cur.length ; ++i ) {
			row.add(int.parse(cur.substring(i,i+1)));
		}
		trees.add(row);
		
		cur = stdin.readLineSync();
	}

	print(trees);
	int total = 0;
	for(int i = 0 ; i < trees.length ; i++){
		for( int j = 0 ; j < trees[0].length ; j++ ){
			if (visible(i,j,trees)) total++;
		}
	}

	print(total);



}

