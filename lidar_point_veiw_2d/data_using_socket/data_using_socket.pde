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
    String[] parts = split(data, ":");
    if (parts.length == 2) {
     // Преобразование полученных значений в float
     float angle = float(parts[0]);
     float distance = float(parts[1]);
     println("Received: " + angle , distance );
  }
 }
}
}
