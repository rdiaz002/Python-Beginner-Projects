#Ronuel Diaz
#Assignment 1
#Python Practice




def fibonacci_sequence (n):
    secondnumber=1;
    first_number=1;
    place_holder=0;
    if(n<=2):
        print(first_number);
    else:
        while(n>2):
            place_holder=first_number+secondnumber;
            first_number=secondnumber;
            secondnumber=place_holder;
            n=n-1;

        print(place_holder);

def cube_natural (m):
    place_holder=0;
    count=0;
    while(count<=m):
        place_holder= place_holder + (count)**3;
        count=count+1
    print(place_holder);





print("what program would you like to run?( input your choice) ");
print("1.Sum of the cubes of the first n natural numbers.\n2.nth Fibonacci number");
j=int(input());

if(j==2):
    n = int(input("what number in the fibonachi sequence would you like?"));

    fibonacci_sequence(n);
elif(j==1):
    m =int(input("add the cube of the natural numbers up to :"));

    cube_natural(m);
else:
    print("choice not valid restart program");
