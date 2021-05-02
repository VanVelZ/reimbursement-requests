from daos.course_dao import CourseDao


class CourseService:
    @staticmethod
    def get_all_courses():
        return CourseDao.get_all_courses()

    @staticmethod
    def get_course(id):
        return CourseDao.get_course(id)
