// https://javarevisited.blogspot.com/2011/12/factory-design-pattern-java-example.html
/*
 So factory pattern solve this problem very easily by model an interface for 
 creating an object which at creation time can let its subclasses decide which 
 class to instantiate, Factory Pattern promotes loose coupling by eliminating 
 the need to bind application-specific classes into the code. The factory methods 
 are typically implemented as virtual methods, so this pattern is also referred 
 to as the "Virtual Constructor". These methods create the objects of the products 
 or target classes.

 Factory method design pattern decouples the calling class from the target class, 
 which result in less coupled and highly cohesive code.

*/

/**
 * Currency
 */
interface Currency {
    String getSymbol();
}

class Rupees implements Currency {
    @Override
    public String getSymbol() {
        return "Rs";
    }
}

class Dollar implements Currency {
    @Override
    public String getSymbol() {
        return "$";
    }
}

class Euro implements Currency {
    @Override
    public String getSymbol() {
        return "Euro";
    }
}

class CurrencyFactory {
    public static Currency createCurrency(String currency) {
        if (currency.equalsIgnoreCase("rupee")) {
            return new Rupees();
        } else if (currency.equalsIgnoreCase("dollar")) {
            return new Dollar();
        } else if (currency.equalsIgnoreCase("euro")) {
            return new Euro();
        } else {
            throw new IllegalArgumentException("Currency does not exists in database");
        }
    }
}

public class Factory_Pattern {
    public static void main(String[] args) {
        Currency dollarCurrency = CurrencyFactory.createCurrency("dollar");
        
        System.out.println(dollarCurrency.getSymbol());
        
        try{
            System.out.println(CurrencyFactory.createCurrency("--new-currency--").getSymbol());
        }catch(Exception e){
            System.out.println(e);
        }
        
        System.out.println(CurrencyFactory.createCurrency("euro").getSymbol());
    }
}
