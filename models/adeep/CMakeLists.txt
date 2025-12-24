cmake_minimum_required(VERSION 3.5)
project(adeep)

# ROS 2 빌드 시스템
find_package(ament_cmake REQUIRED)

# 필요한 의존성 패키지 (예: rclcpp, std_msgs 등)
# 필요하다면 추가하세요
find_package(rclcpp REQUIRED)

# 실행 파일이 있다면 여기에 추가
# add_executable(my_node src/my_node.cpp)
# ament_target_dependencies(my_node rclcpp)

# 설치 규칙: config, launch, meshes, urdf 디렉토리 설치
foreach(dir config launch meshes urdf)
  install(DIRECTORY ${dir}/
    DESTINATION share/${PROJECT_NAME}/${dir})
endforeach()

# 실행 파일 설치 예시
# install(TARGETS
#   my_node
#   DESTINATION lib/${PROJECT_NAME})

ament_package()