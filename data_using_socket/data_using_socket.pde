import processing.net.*;

Client client;

void setup() {
 size(600, 600); // Размер окна
 background(255); // Белый фон
 smooth(); // Включаем сглаживание
 noStroke(); // Отключаем обводку

 // Создание клиента
 client = new Client(this, "127.0.0.1", 65432);

}

void draw() {
 if (client.available() > 0) {
  String data = client.readString();
  if (data != null) {
   // Вывод полученных данных
   println("Received: " + data);
  }
 }
}
