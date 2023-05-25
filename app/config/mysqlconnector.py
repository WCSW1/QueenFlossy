import mysql.connector

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(title, post, photo, postdataFile):
    print("Inserting BLOB into post table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='QueenFlossy_db',
                               )

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO post
                          (title, post, photo, postdata) VALUES (%s,%s,%s,%s)"""

        postImage = convertToBinaryData(photo)
        file = convertToBinaryData(postdataFile)

        # Convert data into tuple format
        insert_blob_tuple = (title, post, postImage, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into post table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
