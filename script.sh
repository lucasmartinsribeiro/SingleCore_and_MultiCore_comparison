rm *.dat

for i in $(seq 2 20)
do
    echo "Interação $i - Single-Core"
    /usr/bin/time -a -o saidaSigleCore.dat -f "$i;\t%e" python3 ./combinacaoSingleCore.py $i

done 

for i in $(seq 2 20)
do
    echo "Interação $i - Multi-Core"
    /usr/bin/time -a -o saidaMultiCore.dat -f "$i;\t%e" mpirun -np 4 python3 ./combinacaoMultiCore.py $i

done 

python3 ./Grafico.py