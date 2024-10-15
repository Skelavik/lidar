import peasy.*;
// PeasyCam cam;

int numPoints = 1068; //10068; // Количество точек
float[][] data = new float[numPoints][3]; // Матрица: [r, theta, phi]
float point_count = 0;

void setup() {
  frameRate(60);
  size(800, 900, P3D);
  smooth();
  noStroke();
  // cam = new PeasyCam(this, 400);
  point_count = TWO_PI / numPoints;
  // println(point_count);

  // Заполнение данных случайными значениями
  for (int i = 0; i < numPoints; i++) {
    data[i][0] = 300; // r (дистанция от центра до точки)
    data[i][1] = i * point_count;  // theta (угол по оси XY)
    data[i][2] = random(0, PI); // phi (угол по оси ZX)
  }
}

void draw() {
  background(20);
  lights(); // Включение освещения для 3D-эксперимента
  // translate(width/2, height/2); // Центрируем на экране
  // rotateY(frameCount * 0.01); // Вращение для эффекта
  
  
  /* ------------------------------------------------------------------*/
  // Модуль упраление камеры
  
  
  float cameraY = height / 2.0;
  float fov = mouseY / float(height) * PI / 2; // Меняем mouseX на mouseY
  float cameraZ = cameraY / tan(fov / 2.0);
  float aspect = float(width) / float(height);
  if (mousePressed) {
      aspect = aspect / 2.0;
  }
  perspective(fov, aspect, cameraZ / 10.0, cameraZ * 10.0);
  
  translate(width / 2 + 30, height / 2, 0);
  rotateX(-PI / 6);
  rotateY(PI / 3 + mouseX / float(width) * PI); // Меняем mouseY на mouseX 


/*---------------------------------------------------------------------*/
 // Отрисовка осей
 // strokeWeight(2);
 // stroke(255, 0, 0); // Красный цвет для оси X
 // line(0, 0, 0, 200, 0, 0); // Ось X
 // stroke(0, 255, 0); // Зеленый цвет для оси Y
 // line(0, 0, 0, 0, 200, 0); // Ось Y
 // stroke(0, 0, 255); // Синий цвет для оси Z
 // line(0, 0, 0, 0, 0, 200); // Ось Z
 // strokeWeight(1);

/*---------------------------------------------------------------------*/  
  for (int i = 0; i < numPoints; i++) {
    float r = data[i][0]; // Длина от центра
    float theta = data[i][1]; // Угол по оси XY
    float phi = data[i][2]; // Угол по оси ZX

    // Преобразование в декартовы координаты
    float x = r * cos(phi) * cos(theta);
    float y = r * cos(phi) * sin(theta);
    float z = r * sin(phi);


// Отрисовка точки
    fill(255, 100, 0); // Цвет точки
    pushMatrix();
    translate(y, -z, x); // Перемещаем на координаты точки
    sphere(1); // Рисуем сферу (точку)
    popMatrix();
  }
}
