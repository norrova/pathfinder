const generateMatrix = (size) => Array(size).fill(Array(size).fill(1));
const getNeighbors = (node, maxLength) => {
    return [
        [node[0] - 1, node[1]],
        [node[0], node[1] + 1],
        [node[0] + 1, node[1]],
        [node[0], node[1] - 1]
    ].filter((node) => 
        node[0] >= 0 && node[0] < maxLength 
        && node[1] >= 0 && node[1] < maxLength
    );
};
const equals = (array, find) => {
    find = JSON.stringify(find);
    for (const elem of array) {
        if (JSON.stringify(elem) === find) return true;
    }
    return false;
};

const getTraces = (node, sizeMatrix, paths = [], path = [node]) => {
    if (JSON.stringify(node) === JSON.stringify(end)) {
        paths.push(path)
    } else {
        getNeighbors(node, sizeMatrix).forEach((node) => {
            if (false === equals(path, node)) {
                getTraces(node, sizeMatrix, paths, [...path, node]);
            }
        });
    }
    return paths;
}


const matrix = generateMatrix(3);
const start  = [0,0];
const end    = [2,2];

const paths = getTraces(start, matrix.length);
paths.forEach((elem, index) => console.log(index, elem.length, elem));
