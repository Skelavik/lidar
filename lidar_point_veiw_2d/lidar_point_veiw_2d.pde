import processing.net.*;

Client client;


int numPoints = 360; // Количество точек, которое будет храниться
float[] distance = new float[numPoints]; // Массив для хранения дистанций
float[] angle = new float[numPoints]; // Массив для хранения углов

float centerX, centerY; // Центр координат для отрисовки
float radius; // Радиус для отрисовки точек
int d = 0;

void setup() {
  size(600, 600); // Размер окна
  background(255); // Белый фон
  smooth(); // Включаем сглаживание
  noStroke(); // Отключаем обводку


  centerX = width / 2; // Центр по горизонтали
  centerY = height / 2; // Центр по вертикали
  radius = min(width, height) / 2 - 20; // Радиус круга для отрисовки

  // Генерация случайных данных
  /*for (int i = 0; i < numPoints; i++) {
    distance[i] = random(55, 60); // Случайное расстояние от 50 до 200
    angle[i] = i; // Случайный угол от 0 до 360 градусов
  }*/
   client = new Client(this, "127.0.0.1", 65432);
}

void draw() {
    
    if (d >= 360) {
      d = 0;
      background(255);
    } else {
      
      
   float x = centerX + radius * cos(radians(angle[d])) * (distance[d] / 100.0); 
   float y = centerY + radius * sin(radians(angle[d])) * (distance[d] / 100.0); 

    fill(255,100,0); // Черный цвет точек
    ellipse(x, y, 5, 5); // Рисуем точку
    
    d++;
    delay(10); 
      
      
    }
    
  
}
  
