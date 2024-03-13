package CA_Basics;

//Here you first declare the name of the variable in between <>

/*

IMPORTANT NOTE:
Do NOT confuse this with Lists along the lesson.
This is a way to take in any kind of class and have undefined variables, NOT a way to hold LISTS !!!


 */
public class Generic_Printer <VariableType> {
    //Then you use it as a 'variable type' when using it
    VariableType thingToPrint ;


    public Generic_Printer(VariableType thingToPrint){
        this.thingToPrint = thingToPrint;

    }
    public void Print(){
        System.out.println(thingToPrint);


    }

}




/*
Generics allows us to avoid repeating any code if we want to input different variable types

Generics prevented me from having to do all this for all type of variables:

--> For String:
public class Generic_Printer {
    String thingToPrint ;
    public Generic_Printer(String thingToPrint){
        this.thingToPrint = thingToPrint;

    }
    public void Print(){
        System.out.println(thingToPrint);
    }
}

--> For int:
public class Generic_Printer {
    int thingToPrint ;
    public Generic_Printer(int thingToPrint){
        this.thingToPrint = thingToPrint;

    }
    public void Print(){
        System.out.println(thingToPrint);
    }
}

--> For double:
public class Generic_Printer {
    double thingToPrint ;
    public Generic_Printer(double thingToPrint){
        this.thingToPrint = thingToPrint;

    }
    public void Print(){
        System.out.println(thingToPrint);
    }
}

--> For boolean:
public class Generic_Printer {
    boolean thingToPrint ;
    public Generic_Printer(boolean thingToPrint){
        this.thingToPrint = thingToPrint;

    }
    public void Print(){
        System.out.println(thingToPrint);
    }
}

    ETC ...

 */