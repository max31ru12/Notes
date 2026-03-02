
Это про то, как изменения одного объекта влияют на связанный объект. 

## Cascading actions in SQLAlchemy

- save-update
- merge
- refresh-expire
- expunge
- delete
- delete-orphan
- all


По дефолту применяются `save-update` и `merge` :

```python
children: Mapped[list["Child"]] = relationship(
	back_populates="parent", cascade="save-update, merge"	
)
```

### save-update

Когда объект добавлен в сессию, связанные модели также добавляются в сессию

```python
parent = Parent()
Child = Child()
parent.children.append(child)

session.add(parent)

assert child in session # True
```

### merge

Когда


### delete

При удалении записи удаляет все связанные записи


### delete-orphan


