import 'dart:io';

class Valve {
	String label ;
	int flow_rate ;
	bool marked ;
	bool open ;
	List<String> neighbors ;

	Valve ({required this.label, 
			required this.flow_rate , 
			this.marked = false, 
			this.open = false, 
			required this.neighbors});
}

class Valves { 
	Map<String,Valve> list ;
	Valve? cur;
	int minute = 1 ;

	Valves({ this.list = const {}, this.cur });
}

Valves parse(){
	Map<String,Valve> list = {} ;
	for ( var line = stdin.readLineSync();line!=null;line = stdin.readLineSync()){
		String s = line ;
		var label = s.substring(6,8);
		var flow_rate = int.parse(s.substring(s.indexOf('=')+1,s.indexOf(';')));
		List<String> neighbors = [];
		var ne = s.substring(s.indexOf('to v')+5);
		print(ne);
		ne = ne.substring(ne.indexOf(' ')+1);
		var done = false ;
		print(ne);
		if (!ne.contains(',') ){
			neighbors.add(ne.substring(0,2));
			done = true ;
		}
		while ( !done ){
			if (!ne.contains(',') ){
				neighbors.add(ne.substring(0,2));
				done = true ;
			}
			if (!done){
				neighbors.add(ne.substring(0,2));
				ne = ne.substring(ne.indexOf(',')+2);
			}
		}
		print(label);
		Valve v = Valve(label:label,flow_rate:flow_rate,neighbors:neighbors);
		list[v.label] = v;
	}
	return Valves(list:list);
}





main(){
	Valves vs = parse();
	vs.cur = vs.list['AA'];
	print(vs.cur);
	print(vs.minute);
	int total = 0 ;
	print(vs.cur?.flow_rate);
	for ( var i in vs.list.keys ){
		print(i);
		var x = vs.list[i];
		if (x != null){
			for (var j in x.neighbors){
			}
		}
	}
}




