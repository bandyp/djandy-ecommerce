{"filter":false,"title":"tests_views.py","tooltip":"/cart/tests_views.py","undoManager":{"mark":75,"position":75,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":25},"action":"remove","lines":["from django.test import TestCase","","# Create your tests here."],"id":2},{"start":{"row":0,"column":0},"end":{"row":4,"column":35},"action":"insert","lines":["from django.test import TestCase","from products.models import Product","from django.contrib.auth.models import User","from django.urls import reverse","from accounts.models import Swimmer"]}],[{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"remove","lines":["r"],"id":3},{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"remove","lines":["e"]},{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"remove","lines":["m"]},{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"remove","lines":["m"]},{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"remove","lines":["i"]},{"start":{"row":4,"column":29},"end":{"row":4,"column":30},"action":"remove","lines":["w"]},{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"remove","lines":["S"]}],[{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"insert","lines":["P"],"id":4},{"start":{"row":4,"column":29},"end":{"row":4,"column":30},"action":"insert","lines":["r"]},{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"insert","lines":["o"]},{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"insert","lines":["f"]},{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"insert","lines":["i"]},{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"insert","lines":["l"]},{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":35},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["c"]},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":["l"]},{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["a"]},{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"insert","lines":["s"]},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":[" "],"id":7},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["T"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["e"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["s"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["V"],"id":8},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["i"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["e"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["w"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":15},"end":{"row":6,"column":17},"action":"insert","lines":["()"],"id":9}],[{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["T"],"id":10},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["e"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["s"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["t"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["C"]}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["a"],"id":11},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["s"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":[":"],"id":12}],[{"start":{"row":6,"column":26},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["d"],"id":14},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["e"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":[" "],"id":15},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["g"]}],[{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["e"],"id":16},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["_"],"id":17},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["h"]},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["o"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":[","]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["m"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"remove","lines":["e"],"id":18},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"remove","lines":["m"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"remove","lines":[","]}],[{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["m"],"id":19},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["e"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["_"]}],[{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["p"],"id":20},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["a"]},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["g"]},{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["e"]},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["w"]}],[{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"remove","lines":["w"],"id":21}],[{"start":{"row":7,"column":21},"end":{"row":7,"column":23},"action":"insert","lines":["()"],"id":22}],[{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["s"],"id":23},{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":["e"]},{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["l"]},{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["f"]}],[{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":[":"],"id":24}],[{"start":{"row":7,"column":28},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":8,"column":0},"end":{"row":8,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["p"],"id":26},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["a"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["g"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":[" "],"id":27},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":[" "],"id":28},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["s"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["l"],"id":29},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["f"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["."]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["c"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["l"]}],[{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["i"],"id":30},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["e"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["n"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["."],"id":31},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["g"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["e"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":32},"action":"insert","lines":["()"],"id":32}],[{"start":{"row":8,"column":31},"end":{"row":8,"column":33},"action":"insert","lines":["\"\""],"id":33}],[{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["/"],"id":34}],[{"start":{"row":8,"column":35},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":9,"column":0},"end":{"row":9,"column":8},"action":"insert","lines":["        "]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["e"],"id":36},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["l"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["f"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["."]}],[{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["a"],"id":37},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["s"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["s"]},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":["e"]},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["r"]},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"insert","lines":["E"],"id":38},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["q"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["u"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["a"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["l"]}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":26},"action":"insert","lines":["()"],"id":39}],[{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["p"],"id":40},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["a"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["g"]},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["."],"id":41},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["s"]},{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"insert","lines":["t"]},{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"insert","lines":["a"]},{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"insert","lines":["t"]},{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"insert","lines":["u"]},{"start":{"row":9,"column":35},"end":{"row":9,"column":36},"action":"insert","lines":["s"]}],[{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"insert","lines":["_"],"id":42}],[{"start":{"row":9,"column":37},"end":{"row":9,"column":38},"action":"insert","lines":["c"],"id":43},{"start":{"row":9,"column":38},"end":{"row":9,"column":39},"action":"insert","lines":["o"]}],[{"start":{"row":9,"column":39},"end":{"row":9,"column":40},"action":"insert","lines":["d"],"id":44},{"start":{"row":9,"column":40},"end":{"row":9,"column":41},"action":"insert","lines":["e"]},{"start":{"row":9,"column":41},"end":{"row":9,"column":42},"action":"insert","lines":[","]}],[{"start":{"row":9,"column":42},"end":{"row":9,"column":43},"action":"insert","lines":[" "],"id":45},{"start":{"row":9,"column":43},"end":{"row":9,"column":44},"action":"insert","lines":["2"]},{"start":{"row":9,"column":44},"end":{"row":9,"column":45},"action":"insert","lines":["0"]},{"start":{"row":9,"column":45},"end":{"row":9,"column":46},"action":"insert","lines":["0"]}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["t"],"id":46},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["e"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["s"]},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["_"],"id":47}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":11},"action":"insert","lines":["self.assert"],"id":48}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "],"id":49}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":8},"action":"insert","lines":["    "],"id":50}],[{"start":{"row":10,"column":19},"end":{"row":10,"column":20},"action":"insert","lines":["T"],"id":51},{"start":{"row":10,"column":20},"end":{"row":10,"column":21},"action":"insert","lines":["e"]},{"start":{"row":10,"column":21},"end":{"row":10,"column":22},"action":"insert","lines":["m"]},{"start":{"row":10,"column":22},"end":{"row":10,"column":23},"action":"insert","lines":["p"]},{"start":{"row":10,"column":23},"end":{"row":10,"column":24},"action":"insert","lines":["l"]},{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"insert","lines":["a"]},{"start":{"row":10,"column":25},"end":{"row":10,"column":26},"action":"insert","lines":["t"]},{"start":{"row":10,"column":26},"end":{"row":10,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":10,"column":27},"end":{"row":10,"column":28},"action":"insert","lines":["U"],"id":52},{"start":{"row":10,"column":28},"end":{"row":10,"column":29},"action":"insert","lines":["s"]},{"start":{"row":10,"column":29},"end":{"row":10,"column":30},"action":"insert","lines":["e"]},{"start":{"row":10,"column":30},"end":{"row":10,"column":31},"action":"insert","lines":["d"]}],[{"start":{"row":10,"column":31},"end":{"row":10,"column":33},"action":"insert","lines":["()"],"id":53}],[{"start":{"row":10,"column":32},"end":{"row":10,"column":33},"action":"insert","lines":["p"],"id":54},{"start":{"row":10,"column":33},"end":{"row":10,"column":34},"action":"insert","lines":["a"]},{"start":{"row":10,"column":34},"end":{"row":10,"column":35},"action":"insert","lines":["g"]},{"start":{"row":10,"column":35},"end":{"row":10,"column":36},"action":"insert","lines":["e"]},{"start":{"row":10,"column":36},"end":{"row":10,"column":37},"action":"insert","lines":[","]}],[{"start":{"row":10,"column":37},"end":{"row":10,"column":38},"action":"insert","lines":[" "],"id":55}],[{"start":{"row":10,"column":38},"end":{"row":10,"column":40},"action":"insert","lines":["\"\""],"id":56}],[{"start":{"row":10,"column":39},"end":{"row":10,"column":40},"action":"insert","lines":["c"],"id":57},{"start":{"row":10,"column":40},"end":{"row":10,"column":41},"action":"insert","lines":["a"]},{"start":{"row":10,"column":41},"end":{"row":10,"column":42},"action":"insert","lines":["r"]},{"start":{"row":10,"column":42},"end":{"row":10,"column":43},"action":"insert","lines":["t"]}],[{"start":{"row":10,"column":43},"end":{"row":10,"column":44},"action":"insert","lines":["."],"id":58},{"start":{"row":10,"column":44},"end":{"row":10,"column":45},"action":"insert","lines":["h"]},{"start":{"row":10,"column":45},"end":{"row":10,"column":46},"action":"insert","lines":["t"]},{"start":{"row":10,"column":46},"end":{"row":10,"column":47},"action":"insert","lines":["m"]},{"start":{"row":10,"column":47},"end":{"row":10,"column":48},"action":"insert","lines":["l"]}],[{"start":{"row":10,"column":42},"end":{"row":10,"column":43},"action":"remove","lines":["t"],"id":59},{"start":{"row":10,"column":41},"end":{"row":10,"column":42},"action":"remove","lines":["r"]},{"start":{"row":10,"column":40},"end":{"row":10,"column":41},"action":"remove","lines":["a"]},{"start":{"row":10,"column":39},"end":{"row":10,"column":40},"action":"remove","lines":["c"]}],[{"start":{"row":10,"column":39},"end":{"row":10,"column":40},"action":"insert","lines":["i"],"id":60},{"start":{"row":10,"column":40},"end":{"row":10,"column":41},"action":"insert","lines":["n"]},{"start":{"row":10,"column":41},"end":{"row":10,"column":42},"action":"insert","lines":["d"]},{"start":{"row":10,"column":42},"end":{"row":10,"column":43},"action":"insert","lines":["e"]},{"start":{"row":10,"column":43},"end":{"row":10,"column":44},"action":"insert","lines":["x"]}],[{"start":{"row":10,"column":51},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":61},{"start":{"row":11,"column":0},"end":{"row":11,"column":8},"action":"insert","lines":["        "]},{"start":{"row":11,"column":8},"end":{"row":12,"column":0},"action":"insert","lines":["",""]},{"start":{"row":12,"column":0},"end":{"row":12,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":8},"action":"remove","lines":["    "],"id":62}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["d"],"id":63},{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["e"]},{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":[" "],"id":64},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["e"],"id":65},{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["t"],"id":66},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["_"]}],[{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["g"],"id":67},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":["e"]},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":16},"action":"remove","lines":["test_get"],"id":68},{"start":{"row":12,"column":8},"end":{"row":12,"column":28},"action":"insert","lines":["test_get_home_page()"]}],[{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"remove","lines":["e"],"id":69},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"remove","lines":["m"]},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"remove","lines":["o"]},{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"remove","lines":["h"]}],[{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":["i"],"id":70},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["t"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["e"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["m"]}],[{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"insert","lines":["s"],"id":71},{"start":{"row":12,"column":28},"end":{"row":12,"column":29},"action":"insert","lines":["e"]},{"start":{"row":12,"column":29},"end":{"row":12,"column":30},"action":"insert","lines":["l"]},{"start":{"row":12,"column":30},"end":{"row":12,"column":31},"action":"insert","lines":["f"]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "],"id":72}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":8},"action":"insert","lines":["    "],"id":73}],[{"start":{"row":13,"column":8},"end":{"row":15,"column":51},"action":"insert","lines":["page = self.client.get(\"/\")","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"index.html\")"],"id":74}],[{"start":{"row":13,"column":33},"end":{"row":13,"column":34},"action":"insert","lines":["a"],"id":75},{"start":{"row":13,"column":34},"end":{"row":13,"column":35},"action":"insert","lines":["d"]},{"start":{"row":13,"column":35},"end":{"row":13,"column":36},"action":"insert","lines":["d"]}],[{"start":{"row":12,"column":32},"end":{"row":12,"column":33},"action":"insert","lines":[":"],"id":76}],[{"start":{"row":12,"column":0},"end":{"row":15,"column":51},"action":"remove","lines":["    def test_get_item_page(self):","        page = self.client.get(\"/add\")","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"index.html\")"],"id":77}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":0},"end":{"row":12,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1582814366718,"hash":"896dbf8c22c7c465798a4a17ab6ec67b9358e06b"}