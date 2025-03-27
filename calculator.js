function add(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}

function multiply(a, b) {
    return a * b;
}

function divide(a, b) {
    if (b === 0) {
        return "Error: Division by zero is not allowed.";
    }
    return a / b;
}

function calculator() {
    console.log("Basic Calculator");
    console.log("Select operation:");
    console.log("1. Add");
    console.log("2. Subtract");
    console.log("3. Multiply");
    console.log("4. Divide");

    const choice = prompt("Enter choice (1/2/3/4):");

    if (["1", "2", "3", "4"].includes(choice)) {
        const num1 = parseFloat(prompt("Enter first number:"));
        const num2 = parseFloat(prompt("Enter second number:"));

        let result;
        switch (choice) {
            case "1":
                result = add(num1, num2);
                break;
            case "2":
                result = subtract(num1, num2);
                break;
            case "3":
                result = multiply(num1, num2);
                break;
            case "4":
                result = divide(num1, num2);
                break;
        }
        console.log(`The result is: ${result}`);
    } else {
        console.log("Invalid input. Please select a valid operation.");
    }
}

// Run the calculator
calculator();