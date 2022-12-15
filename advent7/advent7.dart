import 'dart:io';
List paths = [];
var map = <String,directory> {};
class directory {
	List<String> children;
	String parent;
	List<file> files;
	String name;
	directory(this.children,this.parent,this.files,this.name);
	num get_size(){
		num sum = 0;
		for ( file i in files ){
			sum+=i.size;
		}
		for ( String i in children ){
			sum+=map[this.name + i + '/']!.get_size();
		}
		return sum;
	}
}
class file {
	String name ;
	int size ;
	file(this.name,this.size);
}
main(){
	String curpath = '/';
	directory home = directory([],'',[],'/');
	map.putIfAbsent('/',(){return home;});
	var line = stdin.readLineSync();
	while (line!='' && line!=null){
		line = stdin.readLineSync();
		if ( line == '' || line==null ) break;
		/* print(line); */
		if (line.contains('cd ..')){
			/* print(curpath); */
			curpath = curpath.substring(0,curpath.length - 1);
			curpath = curpath.substring(0,curpath.lastIndexOf('/')+1);
			/* print(curpath); */
		}
		else if (line.contains('cd ')){
			String sub = line.substring(line.indexOf('cd ') + 3);
			curpath += sub + '/' ;
		}
		else if (line.contains('ls ')){}
		else if(line.contains('dir ')) {
			String name = line.substring(line.indexOf('dir ') + 4 );
			directory dir = directory([],curpath,[],curpath+name+'/');
			map.putIfAbsent(curpath+name+'/',(){return dir;});
			paths.add(curpath+name+'/');
			map[curpath]!.children.add(name);
		}
		else if (!line.contains('\$')){
			int size = int.parse(line.substring(0,line.indexOf(' ')));
			String name = line.substring(line.indexOf(' ')+1);
			map[curpath]!.files.add(file(name,size));
		}
	}
	num sum = 0;
	for (var i in paths){
		num n = map[i]!.get_size();
		if ( n <= 100000 ) {
			sum+=n;
		}
	}
	print(sum);
}


