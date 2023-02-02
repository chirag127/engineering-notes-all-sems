### Persisting data using SQLite for the notes of the Unit 4 - TECHNOLOGY I – ANDROID in the subject of Design & Development Of Applications
SQLite is a lightweight, file-based database that can be used to persist data in Android applications. To use SQLite in an Android app, you can use the SQLiteOpenHelper class, which provides a convenient way to manage the database. 

1. First, you need to create a subclass of SQLiteOpenHelper to manage the database. 
2. In the subclass, you need to override the onCreate() and onUpgrade() methods to create and upgrade the database tables, respectively. 
3. To insert data into the database, you can use the SQLiteDatabase.insert() method. 
4. To retrieve data from the database, you can use the SQLiteDatabase.query() method. 
5. To update data in the database, you can use the SQLiteDatabase.update() method. 
6. To delete data from the database, you can use the SQLiteDatabase.delete() method. 

Example code:
```
public class NotesDbHelper extends SQLiteOpenHelper {
  private static final String DATABASE_NAME = "notes.db";
  private static final int DATABASE_VERSION = 1;

  public NotesDbHelper(Context context) {
    super(context, DATABASE_NAME, null, DATABASE_VERSION);
  }

  @Override
  public void onCreate(SQLiteDatabase db) {
    String SQL_CREATE_NOTES_TABLE =  "CREATE TABLE " + NotesContract.NoteEntry.TABLE_NAME + " ("
        + NotesContract.NoteEntry._ID + " INTEGER PRIMARY KEY AUTOINCREMENT, "
        + NotesContract.NoteEntry.COLUMN_NOTE_TITLE + " TEXT NOT NULL, "
        + NotesContract.NoteEntry.COLUMN_NOTE_TEXT + " TEXT NOT NULL);";

    db.execSQL(SQL_CREATE_NOTES_TABLE);
  }

  @Override
  public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
    // The database is still at version 1, so there's nothing to do be done here.
  }
}
```
