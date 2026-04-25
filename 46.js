// Ждём, пока вся страница загрузится, чтобы скрипт ничего не потерял
document.addEventListener('DOMContentLoaded', () => {
    
    // Выцепляем элементы по их ID
    const inputField = document.getElementById('myInput');
    const clearBtn = document.getElementById('clearBtn');
    const sendBtn = document.getElementById('sendBtn');

    // ФУНКЦИЯ ОТПРАВКИ
    const handleSend = () => {
        const message = inputField.value.trim(); // .trim() убирает лишние пробелы по бокам

        if (message === "") {
            // Если в инпуте пусто или одни пробелы
            inputField.style.borderColor = "#ff4d4d"; // Подсветим красным, что юзер тупит
            setTimeout(() => inputField.style.borderColor = "#333", 1000); // Через секунду вернем как было
            console.warn("Пусто, шеф! Писать-то кто будет?");
        } else {
            // Имитируем отправку
            console.log("Сообщение улетело:", message);
            alert("🚀 Отправлено: " + message);
            
            // Очищаем поле после успешной "отправки"
            inputField.value = "";
        }
    };

    // Слушаем клик по кнопке Send
    sendBtn.addEventListener('click', handleSend);

    // Слушаем клик по кнопке Clear
    clearBtn.addEventListener('click', () => {
        if (inputField.value !== "") {
            inputField.value = "";
            console.log("Зачистка произведена успешно.");
        }
    });

    // Добавляем поддержку Enter, чтобы не тыкать мышкой каждый раз
    inputField.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            handleSend();
        }
    });

    console.log("Система запущена. Кодер — гений!");
});