export const random = ( random : Array<string> ) => {
    return random[Math.floor(Math.random() * random.length)];
}