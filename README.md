# Tugas3Kelompok
## Anggota
- Fitrah Arie Ramadhan 05111940000025
- Julietta Anastasia Rodiah Boru Panjaitan 05111940000033
- Nabil Fikri Arief 05111940000086
- Gerry Sihaj 05111940000124
- Ryan Fernaldy 05111940000152

Penyelesaian kasus Rat in a Maze dengan menggunakan Greedy Best First Search dan A* Search

Untuk nilai dari heuristic nya menggunakan heuristic euclidean (mencari jarak sejati dari titik node dengan titik finish) menggunakan pythagoras

maze=[

    ['#','#','#','#','#','G','#','#'],
    
    ['#','#','#','#',' ',' ',' ','#'],
    
    [' ',' ',' ',' ',' ','#',' ',' '],
    
    [' ','#','#','#','#','#','#',' '],
    
    [' ','S',' ',' ',' ',' ',' ',' ']
]

Dari Maze ini diminta untuk mencari jalan tercepat dari initial State yaitu G ke S sebagai goal state.

Analisis dari soal ini didapatkan ternyata terbukti waktu dan langkah terbaik dan maksimal terdapat di metode A* search dengan hasil yang didapatkan.
Adapun hasil yang didapatkan adalah sebagai berikut 
1. Searching dengan menggunakan Greedy Best First Search adalah sebagai berikut Ditemukan setelah melakukan ekspansi sebanyak 13 node
dengan 12 langkah: ['RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT', 'UP']
Waktunya adalah  0.0009846687316894531
2. Searching dengan menggunakan A* adalah sebagai berikut Ditemukan setelah melakukan ekspansi sebanyak 16 node
dengan 10 langkah: ['LEFT', 'UP', 'UP', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'UP', 'RIGHT', 'UP']
Waktunya adalah  0.0009639263153076172

Hasil yang didapatkan setelah dianalisis terdapat perbedaan waktu kecepatan serta hasil yang didapatkan. Dapat disimpulkan bahwasannya Searching dengan menggunakan A* lebih maksimal dengan hanya 10 langkah sedangkan Greedy Best First Search didapatkan 12 langkah dengan waktu yang lebih lama dan tidak mendapatkan hasil yang diinginkan. Oleh karena itu dari analisis ini terdapat kesimpulan yaitu algoritma A* lebih baik daripada Greedy Best First Search.
