function convertDecimalToOthers() {
    const decimalInput = document.getElementById("decimalInput").value;
    const binaryInput = document.getElementById("binaryInput");
    const hexInput = document.getElementById("hexInput");

    // Conversion décimale en binaire
    const decimalValue = parseInt(decimalInput, 10);
    const binaryValue = (decimalValue >>> 0).toString(2);
    binaryInput.value = binaryValue;

    // Conversion décimale en hexadécimal
    const hexValue = (decimalValue >>> 0).toString(16).toUpperCase();
    hexInput.value = hexValue;
}

function convertBinaryToOthers() {
    const binaryInput = document.getElementById("binaryInput").value;
    const decimalInput = document.getElementById("decimalInput");
    const hexInput = document.getElementById("hexInput");

    // Conversion binaire en décimal
    const binaryValue = parseInt(binaryInput, 2);
    decimalInput.value = binaryValue;

    // Conversion décimal en hexadécimal
    const hexValue = binaryValue.toString(16).toUpperCase();
    hexInput.value = hexValue;
}

function convertHexToOthers() {
    const hexInput = document.getElementById("hexInput").value;
    const decimalInput = document.getElementById("decimalInput");
    const binaryInput = document.getElementById("binaryInput");

    // Conversion hexadécimale en décimal
    const hexValue = parseInt(hexInput, 16);
    decimalInput.value = hexValue;

    // Conversion décimal en binaire
    const binaryValue = hexValue.toString(2);
    binaryInput.value = binaryValue;
}
