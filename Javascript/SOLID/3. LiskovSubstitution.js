class Rectangle {
  constructor(width, height) {
    this._width = width;
    this._height = height;
  }

  get width() {
    return this._width;
  }

  get height() {
    return this._height;
  }

  set width(value) {
    this._width = value;
  }

  set height(value) {
    this._height = value;
  }

  get area() {
    return this._width * this._height;
  }

  toString() {
    return `${this._width} x ${this._height}`;
  }
}

// Square class not required. It violates LSP
class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }

  set width(value) {
    this._width = this._height = value;
  }

  set height(value) {
    this._width = this._height = value;
  }
}

let useIt = function (rc) {
  let width = rc._width;
  rc.height = 10;
  let expected = width * 10;
  console.log(`Expected area ${expected}, but got ${rc.area}`);
};

let rc = new Rectangle(2, 3);
useIt(rc);

let sq = new Square(5);
useIt(sq);

// sq.width = 10;
// console.log(sq.toString());
