// Получаем кнопки "Редактировать" и "Сохранить" по их идентификаторам
const editButton = document.getElementById(`edit-button-${product.id}`);
const saveButton = document.getElementById(`save-button-${product.id}`);

// Добавляем обработчик события клика на кнопку "Редактировать"
editButton.addEventListener('click', () => {
    // Отключаем кнопку "Редактировать"
    editButton.disabled = true;
    // Включаем кнопку "Сохранить"
    saveButton.disabled = false;
});